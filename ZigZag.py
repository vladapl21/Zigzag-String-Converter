class Solution(object):
  def convert(self, s, numRows):
      """
      :type s: str
      :type numRows: int
      :rtype: str
      """
      if numRows == 1:
          return s
      matrix = [[] for x in range(numRows)]
      pointer = 0
      increasing = True

      for i in range(len(s)):
          matrix[pointer].append(s[i])
          if increasing:
              if pointer == (numRows-1):
                  increasing = False
                  pointer -= 1     
              else:
                  pointer += 1
          elif not increasing:
              if pointer == 0:
                  pointer += 1
                  increasing = True
              else:
                  pointer -= 1

      out = ""
      for x in matrix:
          for j in x:
              if j != []:
                  out = out + j
      return out
