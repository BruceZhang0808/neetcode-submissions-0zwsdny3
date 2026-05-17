class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        nums = []
        for t in tokens:
            if t not in operators:
                nums.append(int(t))
            else:
                suf = nums.pop()
                pre = nums.pop()
                match t:
                    case '+': res = pre + suf
                    case '-': res = pre - suf
                    case '*': res = pre * suf
                    case '/': res = int(pre / suf)
                nums.append(res)
        return nums.pop()