#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import datetime
import argparse
import urllib.request
import json
import sys
import io


def get_weather():
    response = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=200010')
    jsn = json.loads(response.read().decode('utf-8'))
    telop = jsn['forecasts'][0]['telop']
    tmp = jsn['forecasts'][0]['temperature']
    cmax = ''
    cmin = ''
    if tmp['max']:
        cmax = tmp['max']['celsius']
    if tmp['min']:
        cmin = tmp['min']['celsius']
    ts = ''
    if len(cmax) and len(cmin):
        ts = ' ' + cmin + '~' + cmax + '°'
    length = len(telop)*2 + len(ts)+1
    return telop + ts, length


def get_date(weather=False):
    now = datetime.datetime.now()
    d = '%d-%02d-%02d %02d:%02d:%02d' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
    length = len(d)
    if weather:
        w, l = get_weather()
        d += ' ' + w
        length += l
    return d + '\n' + (length * '=')


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    parser = argparse.ArgumentParser(description='Show date with line')
    parser.add_argument('-w', '--weather', action='store_true', help='Show weather')
    args = parser.parse_args()

    dateline = get_date(weather=args.weather)
    print(dateline)

    sys.exit(0)


if __name__ == '__main__':
    main()
