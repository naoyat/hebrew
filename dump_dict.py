import click
import hebrew

@click.command()
def dump_dict():
    for heb, lat, pos, trans in hebrew.dict_stream():
        # print ('(%s) (%s) %s. %s' % (lat, heb, pos, trans)).encode('utf-8')
        print ('%s,%s' % (lat, heb)).encode('utf-8')

if __name__ == '__main__':
    dump_dict()
