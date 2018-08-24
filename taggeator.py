#!/usr/bin/env python
import argparse
import logging
import yaml
from collections import defaultdict
from jinja2 import Template

logger = logging.getLogger(__name__)


def invert(apps):
    result = defaultdict(list)
    for app in apps['apps']:
        for tag in app['tags']:
            result[tag].append(app)
    return result


def init_logging(debug=0):
    levels = (
        logging.WARNING,
        logging.INFO,
        logging.DEBUG,
    )
    level = levels[min(debug, len(levels) - 1)]
    formatter = logging.Formatter(
        '** %(asctime)s.%(msecs)03d %(levelname)s: [%(name)s] %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    handler.setLevel(level)
    logger.setLevel(level)
    logger.addHandler(handler)


def parse_args():
    parser = argparse.ArgumentParser(
        description='generates a page with categorized items'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='count',
        default=0,
        help='Increases verbosity'
    )
    parser.add_argument(
        '-f', '--filename',
        default="categories.yaml",
        help="Input filename"
    )
    parser.add_argument(
        '-o', '--output',
        default="categories.html",
        help="Output filename"
    )
    parser.add_argument(
        '-t', '--template',
        default='categories.jinja',
        help="Template to be used"
    )

    return parser.parse_args()


def main():
    args = parse_args()
    init_logging(args.verbose)

    logger.debug("Verbose mode enabled")

    logger.debug("Load input data")
    with open(args.filename) as fd:
        apps = yaml.load(fd)

    logger.debug("Invert categories")
    categories = invert(apps)

    logger.debug("Load template")
    with open(args.template) as fd:
        template = Template(fd.read())

    logger.info("Applying template")
    with open(args.output, "w+") as fd:
        fd.write(template.render(categories=categories))

if  __name__ == "__main__":
    main()
