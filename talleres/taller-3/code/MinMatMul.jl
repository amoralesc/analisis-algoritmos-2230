module MinMatMul

function min_mat_mul_backtracking(D)
    M = [0 for i = 1:(length(D) - 1), j = 1:(length(D) - 1)]
    B = [0 for i = 1:(length(D) - 1), j = 1:(length(D) - 1)]
    
    for i in (length(D) - 2):-1:1
        for j in (i + 1):(length(D) - 1)
            best = Inf
            for k in i:(j - 1)
                cur = M[i, k] + M[k + 1, j] + D[i] * D[k + 1] * D[j + 1]
                if cur < best
                    best = cur
                    B[i, j] = k
                end
            end
            M[i, j] = best
        end
    end
    return B
end

function draw_parentheses(B, i, j)
    if i == j
        return "A" * string(i)
    else
        k = B[i, j]
        left = draw_parentheses(B, i, k)
        if i != k
            left = "(" * left * ")"
        end
        right = draw_parentheses(B, k+1, j)
        if k+1 != j
            right = "(" * right * ")"
        end
        return left * right
    end
end

function min_mat_mul(D)
    B = min_mat_mul_backtracking(D)
    return draw_parentheses(B, 1, length(D) - 1)
end

export min_mat_mul
end
