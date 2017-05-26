#Lab project
#Ricardo Ruiz 501#

#operations
def get_a(comp,att):
    return ((comp/att)-.3) * 5

def get_b(yds,att):
    return ((yds/att)-3) * 0.25

def get_c(td,att):
    return (td/att) * 20

def get_d(inter,att):
    return 2.375 - ((inter/att)*25)

def passing_rating(comp,att,yds,td,inter):
    #get values
    a = get_a(comp,att)
    b = get_b(yds,att)
    c = get_c(td,att)
    d = get_d(inter,att)

    #return rating
    return ((a+b+c+d)/6) * 100
