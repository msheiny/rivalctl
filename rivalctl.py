#!/usr/bin/env python
import sys
from rival import *
import argparse

def send_reports(reports):
    for report in reports:
        send(report)

def main(args):
    reports = []
    if args.reset:
        reports = FACTORY_PROFILE.to_report_list()
    if args.logo_color is not None:
        reports.append(set_logo_color(args.logo_color))
    if args.logo_style is not None:
        reports.append(set_logo_style(args.logo_style))
    if args.wheel_color is not None:
        reports.append(set_wheel_color(args.wheel_color))
    if args.wheel_style is not None:
        reports.append(set_wheel_style(args.wheel_style))
    if args.cpi1 is not None:
        reports.append(set_cpi_1(args.cpi1))
    if args.cpi2 is not None:
        reports.append(set_cpi_2(args.cpi2))
    if args.polling_rate is not None:
        reports.append(set_polling_rate(args.polling_rate))
    if args.commit:
        reports.append(commit())
    send_reports(reports)


parser = argparse.ArgumentParser()
parser.add_argument('--commit', help="Save to firmware", default=False, action='store_true')
parser.add_argument("--reset", help="Reset all options to FACTORY defaults", action='store_true', default=False)
parser.add_argument("--wheel-color", type=str, metavar="COLOR", help="any valid css color name or hex string")
parser.add_argument("--wheel-style", type=str, metavar="STYLE", help="LED Style [1=Steady, 2-4=Breathe Speed]")
parser.add_argument("--logo-color", type=str, metavar="COLOR", help="any valid css color name or hex string")
parser.add_argument("--logo-style", type=str, metavar="STYLE", help="LED Style [1=Steady, 2-4=Breathe Speed]")

parser.add_argument("--cpi1", type=int, metavar="CPI", help="50-6500 in increments of 50 [default 800]")
parser.add_argument("--cpi2", type=int, metavar="CPI", help="50-6500 in increments of 50 [default 1600]")

parser.add_argument("--polling-rate", metavar="RATE", type=int, help="1000, 500, 250, or 125 [default=1000]")

if __name__ == '__main__':
    args = parser.parse_args()
    if len(sys.argv)==1:
        parser.print_help()
    main(args)
    sys.exit(1)
