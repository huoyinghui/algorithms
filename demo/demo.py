import datetime
import time

if __name__ == '__main__':
    print(time.time())
    d = datetime.datetime.utcnow()
    n = datetime.datetime.now()
    t_d = d.timestamp()
    t_n = n.timestamp()
    print(d.time(), n.time())
    print(d.timetz(), n.timetz())
    # print(d.tzinfo(), n.tzinfo())
    print(d.tzname(), n.tzname())
    print(d.utctimetuple(), n.timetuple())
    print(d.timetuple(), n.timetuple())
    time.mktime(d.utctimetuple())
    print(t_d, t_n)
