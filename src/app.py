from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from os import system

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# <---- DATABASE ---->
db = SQLAlchemy(app)

class Target(db.Model):
    __tablename__ = 'target'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    domain = db.Column(db.String)

    def __init__(self, domain):
        self.domain = domain

db.create_all()


# <---- fastRecon - Command Line Tool ---->
def fastRecon(target):
    system("python3 engine/fastrecon.py {}".format(target))

@app.route('/')
def index():
    targetList = Target.query.all()
    totalTargets = Target.query.filter_by().count()
    return render_template('index.html', targetList=targetList, totalTargets=totalTargets)

@app.route('/recon')
def recon():
    return render_template('recon.html')


@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        domain = request.form.get('domain')
        fastRecon(domain)
        dig = "engine/results/{}/dig.txt".format(domain)
        host =  "engine/results/{}/host.txt".format(domain)
        subdomainEnumeration = "engine/results/{}/subdomain-enumeration.txt".format(domain)
        subdomainBrute = "engine/results/{}/subdomain-bruteforce.txt".format(domain)
        ips = "engine/results/{}/ips.txt".format(domain)
        nmap = "engine/results/{}/nmapOutput.txt".format(domain)


        if domain:
            t = Target(domain)
            db.session.add(t)
            db.session.commit()

        with open(dig) as digfile:
            diginfo = []
            for line in digfile:
                diginfo.append(line)

        with open(host) as hostfile:
            hostinfo = []
            for line in hostfile:
                hostinfo.append(line)

        with open(subdomainEnumeration) as file_in:
            subdomainList = []
            for line in file_in:
                subdomainList.append(line)

        with open(subdomainBrute) as file_in:
            subdomainBruteList = []
            for line in file_in:
                subdomainBruteList.append(line)

        with open(ips) as file_in:
            ipList = []
            for line in file_in:
                ipList.append(line)

        with open(nmap) as file_in:
            nmapList = []
            for line in file_in:
                nmapList.append(line)


        domain = domain.upper()
        targetList = Target.query.all()
        return render_template('report.html',
                               subdomainEnumeration=subdomainList,
                               subdomainBrute=subdomainBruteList,
                               diginfo=diginfo,
                               hostinfo=hostinfo,
                               targetList=targetList,
                               domain=domain,
                               ipList=ipList,
                               nmapList=nmapList)



@app.route('/view', methods=['GET', 'POST'])
def view():
    if request.method == 'POST':
        domain = request.form.get('domain')
        dig = "engine/results/{}/dig.txt".format(domain)
        host =  "engine/results/{}/host.txt".format(domain)
        subdomainEnumeration = "engine/results/{}/subdomain-enumeration.txt".format(domain)
        subdomainBrute = "engine/results/{}/subdomain-bruteforce.txt".format(domain)
        ips = "engine/results/{}/ips.txt".format(domain)
        nmap = "engine/results/{}/nmapOutput.txt".format(domain)

        with open(dig) as digfile:
            diginfo = []
            for line in digfile:
                diginfo.append(line)

        with open(host) as hostfile:
            hostinfo = []
            for line in hostfile:
                hostinfo.append(line)

        with open(subdomainEnumeration) as file_in:
            subdomainList = []
            for line in file_in:
                subdomainList.append(line)

        with open(subdomainBrute) as file_in:
            subdomainBruteList = []
            for line in file_in:
                subdomainBruteList.append(line)

        with open(ips) as file_in:
            ipList = []
            for line in file_in:
                ipList.append(line)

        with open(nmap) as file_in:
            nmapList = []
            for line in file_in:
                nmapList.append(line)

        domain = domain.upper()
        targetList = Target.query.all()
        return render_template(
            'view.html',
            subdomainEnumeration=subdomainList,
            subdomainBrute=subdomainBruteList,
            diginfo=diginfo,
            hostinfo=hostinfo,
            targetList=targetList,
            domain=domain,
            ipList=ipList,
            nmapList=nmapList)

@app.route('/delete/<int:id>')
def delete(id):
    t = Target.query.filter_by(_id = id).first()
    domain = t.domain

    system("rm -r engine/results/{}".format(domain))
    db.session.delete(t)
    db.session.commit()

    targetList = Target.query.all()
    totalTargets = Target.query.filter_by().count()
    return render_template('index.html', targetList=targetList, totalTargets=totalTargets)

@app.route('/spider/<domain>')
def spider(domain):
    spider = "engine/results/{}/spider.txt".format(domain)
    with open(spider) as file_in:
        spiderList = []
        for line in file_in:
            spiderList.append(line)
    return render_template("spider.html", spiderList=spiderList)

@app.route('/waybackurls/<domain>')
def waybackurls(domain):
    waybackurls = "engine/results/{}/waybackurls.txt".format(domain)
    with open(waybackurls) as file_in:
        waybackurlsList = []
        for line in file_in:
            waybackurlsList.append(line)
    return render_template("waybackurls.html", waybackurlsList=waybackurlsList)

@app.route('/screenshots/<domain>')
def screenshots(domain):
    aquatone_folder = "engine/results/{}/aquatone".format(domain)
    system("cp -r {} templates/".format(aquatone_folder))
    return render_template('aquatone/aquatone_report.html')

if __name__ == '__main__':
    app.run(debug=True, port=8081)
