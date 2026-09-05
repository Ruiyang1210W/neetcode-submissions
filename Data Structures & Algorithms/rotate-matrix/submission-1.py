class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bot = l, r

                # save the topleft
                topleft = matrix[top][l + i]

                #move bot left into top left
                matrix[top][l + i] = matrix[bot - i][l]

                #move bot right into bot left
                matrix[bot - i][l] = matrix[bot][r - i]

                #move top right into bot right
                matrix[bot][r - i] = matrix[top + i][r]

                #move top left to top right
                matrix[top +i][r] = topleft
            r -= 1
            l += 1