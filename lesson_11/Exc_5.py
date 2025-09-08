class SuperStr(str):
    def is_repeatance(self, s):

        if not isinstance(s, str) or len(s) == 0 or len(self) == 0:
            return False
        if len(self) % len(s) != 0:
            return False
        repeat_count = len(self) // len(s)
        return self == s * repeat_count

    def is_palindrom(self):
        s = self.lower()
        return s == s[::-1]

s = SuperStr("abcabcabc")
print(s.is_repeatance("abc"))
print(s.is_repeatance("ab"))

p = SuperStr("Bob")
print(p.is_palindrom())
print(SuperStr("hello").is_palindrom())
print(SuperStr("").is_palindrom())