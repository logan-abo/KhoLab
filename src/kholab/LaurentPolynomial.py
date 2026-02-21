class LaurentPolynomial:


    def __init__(self, terms=None):
        """
        Initialize with a dictionary {exponent: coefficient}.
        Only non-zero coefficients are stored.
        """
        if terms is None:
            self.terms = {}
        else:
            # Clean input to ensure we only store non-zero values
            self.terms = {int(k): int(v) for k, v in terms.items() if v != 0}

    def __add__(self, other):
        if not isinstance(other, LaurentPolynomial):
            return NotImplemented
        
        new_terms = self.terms.copy()
        for exp, coeff in other.terms.items():
            new_val = new_terms.get(exp, 0) + coeff
            if new_val == 0:
                new_terms.pop(exp, None)
            else:
                new_terms[exp] = new_val
        return LaurentPolynomial(new_terms)

    def __sub__(self, other):
        if not isinstance(other, LaurentPolynomial):
            return NotImplemented
        
        new_terms = self.terms.copy()
        for exp, coeff in other.terms.items():
            new_val = new_terms.get(exp, 0) - coeff
            if new_val == 0:
                new_terms.pop(exp, None)
            else:
                new_terms[exp] = new_val
        return LaurentPolynomial(new_terms)

    def __mul__(self, other):
        if not isinstance(other, LaurentPolynomial):
            return NotImplemented
        
        # Polynomial multiplication: sum of (c1*c2) * A^(e1+e2)
        new_terms = {}
        for e1, c1 in self.terms.items():
            for e2, c2 in other.terms.items():
                exp = e1 + e2
                coeff = c1 * c2
                new_terms[exp] = new_terms.get(exp, 0) + coeff
        
        return LaurentPolynomial(new_terms)

    def __pow__(self, power):
        if not isinstance(power, int):
            return NotImplemented
        
        if power < 0:
            raise ValueError("Negative exponents are not supported for LaurentPolynomials yet.")
        
        # Identity: poly^0 = 1 (represented as {0: 1})
        if power == 0:
            return LaurentPolynomial({0: 1})
        
        # Start with the identity and multiply
        result = LaurentPolynomial({0: 1})
        base = self
        
        # Efficient power by squaring
        while power > 0:
            if power % 2 == 1:
                result = result * base
            base = base * base
            power //= 2
            
        return result


    def __repr__(self):
        if not self.terms:
            return "0"
        
        # Sort by exponent for a readable string representation
        sorted_exps = sorted(self.terms.keys(), reverse=False)
        parts = []
        for e in sorted_exps:
            c = self.terms[e]
            if e == 0:
                parts.append(f"{c}")
            elif e == 1:
                parts.append(f"{c}A")
            else:
                parts.append(f"{c}A^{e}")
        
        return " + ".join(parts).replace("+ -", "- ")