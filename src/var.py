class Expression(object):
    def __init__(self, terms):
        self.terms = terms

    def __add__(self, other):
        new = self.copy()
        for i in range(len(other.terms)):
            for j in range(len(self.terms)):
                term1 = other.terms[i]
                term2 = self.terms[j]
                if term1.equal_vars(term2):
                    new.terms[i].constant += term2.constant
                    break
            else:
                new.terms.append(other.terms[i].copy())
        return new

    def copy(self):
        new = Expression([])
        for term in self.terms:
            new.terms.append(term.copy())
        return new

    def __repr__(self):
        return " + ".join([str(t) for t in self.terms])

    def __mul__(self, other):
        new = Expression([])
        if isinstance(other, int):
            for term in new.terms:
                term.constant *= other
            return new

        for term1 in other.terms:
            for term2 in self.terms:
                new += Expression([term1 * term2])
        return new

class Term(object):
    def __init__(self, constant = 1, vars = {}):
        self.vars = vars.copy()
        self.constant = constant

    def __repr__(self):
        return "%i%s" % (self.constant, "".join([c + ("^" + str(self.vars[c])) * (self.vars[c] != 1) for c in sorted(self.vars.keys())]))

    def __getitem__(self, key):
        return self.vars[key]

    def __setitem__(self, key, item):
        self.vars[key] = item

    def __contains__(self, key):
        return key in self.vars

    def __rmul__(self, other):
        return self.__mul__(other)

    def __mul__(self, other):
        if isinstance(other, int):
            new = self.copy()
            new.constant *=  other
            return new
        new = Term(self.constant * other.constant, self.vars.copy())
        for var in other.vars:
            if var in self:
                new[var] += other[var]
            else:
                new[var] = other[var]
        return new

    def __eq__(self, other):
        return (self.constant == other.constant) and (self.vars == other.vars)

    def equal_vars(self, other):
        return self.vars == other.vars

    def __add__(self, other):
        assert equal_vars(self, other), "%s and %s aren't compatible terms" % (self, other)
        return Term(self.constant + other.constant, self.vars.copy())

    def copy(self):
        return Term(self.constant, self.vars.copy())
