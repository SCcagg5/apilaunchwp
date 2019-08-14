from Model.basic import check
from Object.evts import evts

def deploy(cn, nextc):
    err = check.contain(cn.pr, ["number", "login"])
    if not err[0]:
        return cn.toret.add_error(err[1], err[2])
    err = evts.run(cn.pr["number"], cn.pr["login"])
    return cn.call_next(nextc, err)
