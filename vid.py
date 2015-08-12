import urllib2
filename = 'bookofeli.mp4'

f = open(filename, 'wb')

r = urllib2.urlopen('http://103.43.94.65:8081/vod/m/1037705.mp4?wmsAuthSign=c2VydmVyX3RpbWU9Ny8xNy8yMDE1IDEyOjI3OjIzIEFNJmhhc2hfdmFsdWU9cEFYR0dEN2FRcjhjamhDN0hoek9uQT09JnZhbGlkbWludXRlcz0yMA==&nimblesessionid=597410')

block_size = 64
while True:
    try:
        buffer = r.read(block_size)
        if not buffer:
            break
        f.write(buffer)
    except:
        print 'error'
f.close()
