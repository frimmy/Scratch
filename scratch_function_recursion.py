class Fibo(object):		
	def fibo(self,n):
		a, b = 0, 1
		terms = [a,b]
		i = n
		while len(terms) <= n+1:
			b += a
			terms.append(b)
			a = terms[len(terms)-2]
		return a


class FiboRecur(object):
	def fibo_recur(self,n):
		if n < 2:
			return n
		else:
			return self.fibo_recur(n-1)+self.fibo_recur(n-2)
