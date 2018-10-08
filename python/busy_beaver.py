# coding -*- utf-8
import random
from copy import copy, deepcopy
from random import randrange, randint
import functools
import json

never_end = {'a0': 'c1r', 'a1': 'c0l', 'b1': 'e0r', 'c0': 'd1r', 'c1': 'c1l', 'd0': 'e1l', 'd1': 'b0r',
             'e0': 'e1l', 'e1': 'a1l'}
# never_end = {'a0': 'd1r', 'a1': 'b0r', 'b0': 'b1r', 'b1': 'e0r', 'c1': 'c0l', 'c0': 'b0l',
#              'd0': 'c1l', 'e0': 'a1r', 'e1': 'd0l'}

# never_end = {'a1': 'b1r', 'a1': 'c1l', 'b0': 'c1r', 'b1': 'b1r', 'c0': 'e1r',
#              'c1': 'd0l', 'd0': 'a1l', 'd1': 'd1l', 'e0': 'f1r', 'f1': 'a0l'}


directions = ['r', 'l']
NUMBER = 500

class BusyBeaver(object):
    def __init__(self, state_num):
        self.state_num = state_num
        self.start = 'a'
        self.end = chr(ord(self.start) + self.state_num)

    def judge(self, rule):
        tape = ['0']
        index = 0
        step = 0
        status = 'a'
        while True:
            if status == self.end:
                break
            length = len(tape)
            t = status + tape[index]
            value = rule.get(t, '')
            if not value:
                break
            next_status, symbol, direction = value[0], value[1], value[2]
            tape[index] = symbol
            status = next_status
            if direction == 'r':
                if index == length - 1:
                    tape.append('0')
                index += 1
            else:
                if index == 0:
                    tape.insert(0, '0')
                else:
                    index -= 1
            step += 1
            if step > 5000:
                return 0
        # if step > 10:
        #     f = open("rules.txt", "a")
        #     json.dumps(rule, f)
        #     f.close()
        return step

    def new_rule(self):
        status = chr(ord('a') + randrange(self.state_num))
        current = '%d' % randrange(2)
        next_status = chr(ord('a') + randrange(self.state_num + 1))
        next_symbol = '%d' % randrange(2)
        direction = directions[randrange(2)]
        return status + current, next_status + next_symbol + direction

    def generate_rule(self):
        rule = {}
        for i in range(randint(20, 22)):
            key, value = self.new_rule()
            rule[key] = value
        return rule

    def mution(self, rule):
        r = random.random()
        if r < 0.5:
            keys = list(rule.keys())
            i = randrange(len(keys))
            value = rule[keys[i]]
            status, symbol, direction= value[0], value[1], value[2]
            j = randrange(2)
            if j == 1:
                direction = directions[randrange(2)]
            else:
                k = randrange(2)
                if k == 0:
                    status = chr(ord('a') + randrange(self.state_num + 1))
                else:
                    symbol = '%d' % randrange(2)
            rule[keys[i]] = status + symbol + direction
        else:
            key, value = self.new_rule()
            rule[key] = value

    def cross(self, ra, rb):
        ka = list(ra.keys())
        kb = list(rb.keys())
        i = randrange(len(ka))
        j = randrange(len(kb))
        ra[ka[i]], rb[kb[j]] = rb[kb[j]], ra[ka[i]]

    def child(self, a, b):
        ra = copy(a)
        rb = copy(b)
        self.cross(ra, rb)
        r = random.random()
        rc = {}
        if r < 0.5:
            rc = ra
        else:
            rc = rb
        r = random.random()
        if r < 0.3:
            self.mution(rc)
        return rc

    def get_best(self, rules):
        value = 0
        best = {}
        for rule in rules:
            v = self.judge(rule)
            if v > value:
                best = rule
                value = v
        return best

    def next(self, rules, n=1):
        while n > 0:
            newrules = deepcopy(rules)
            length = len(rules)
            i = 0
            other = self.generate(NUMBER)
            while i < length:
                ra = random.choice(rules)
                rb = random.choice(other)
                rc = self.child(ra, rb)
                newrules.append(rc)
                i = i + 1
            newrules.sort(key=functools.cmp_to_key(self.compare))
            rules = newrules[:500]
            n -= 1
            print(self.get_best_result(rules))
            print(self.get_best(rules))
            self.print_values(rules[:50])
            print("genertation %d " % n)

    def compare(self, ra, rb):
        return self.judge(rb) - self.judge(ra)

    def print_values(self, rules):
        value = []
        for rule in rules:
            value.append(self.judge(rule))
        print(value)

    def get_best_result(self, rules):
        best = 0
        for rule in rules:
            v = self.judge(rule)
            if best < v:
                best = v
        return best

    def generate(self, n):
        rules = []
        for x in range(n):
            r = self.generate_rule()
            if self.judge(r) > 1:
                rules.append(r)
        return rules

    def run(self):
        rules = self.generate(NUMBER)
        rules.sort(key=functools.cmp_to_key(self.compare))
        self.next(rules, 10000)
        print(self.get_best_result(rules))


if __name__ == '__main__':
    busy_beaver = BusyBeaver(4)
    print(busy_beaver.run())
    # for i in range(2, 5):
    #     busy_beaver = BusyBeaver(i)
    #     print(busy_beaver.run())

