#!/usr/bin/env python3
"""Analyze simulated SSH authentication logs for repeated failures."""

import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path

FAIL_RE = re.compile(
    r"Failed password for (?:invalid user )?(?P<user>\S+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})"
)
SUCCESS_RE = re.compile(
    r"Accepted password for (?P<user>\S+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})"
)


def analyze(path: Path):
    failures = Counter()
    targeted_users = defaultdict(set)
    successes = []

    for line in path.read_text(encoding="utf-8").splitlines():
        fail = FAIL_RE.search(line)
        if fail:
            ip = fail.group("ip")
            failures[ip] += 1
            targeted_users[ip].add(fail.group("user"))
            continue

        success = SUCCESS_RE.search(line)
        if success:
            successes.append((success.group("ip"), success.group("user")))

    print("Failed authentication summary")
    print("=" * 50)
    for ip, count in failures.most_common():
        users = ", ".join(sorted(targeted_users[ip]))
        flag = "  <-- REVIEW" if count >= 5 else ""
        print(f"{ip:15} failures={count:2} users={users}{flag}")

    print("\nSuccessful logins")
    print("=" * 50)
    if not successes:
        print("None")
    else:
        for ip, user in successes:
            marker = "  <-- success after observed failures" if ip in failures else ""
            print(f"{ip:15} user={user}{marker}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("logfile", type=Path)
    args = parser.parse_args()

    if not args.logfile.is_file():
        raise SystemExit(f"File not found: {args.logfile}")

    analyze(args.logfile)


if __name__ == "__main__":
    main()
