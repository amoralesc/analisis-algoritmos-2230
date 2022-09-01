#=
Execution instructions:

    $ julia run_experiment.jl <experiments_file>

    <experiments_file>: path to the CSV file containing the experiments to run
    an example is provided in the experiments.csv file
=#

include("./MinMatMul.jl")
using .MinMatMul

# Read the file containing the experiments
file_path = ARGS[1]
file = open(file_path, "r")
experiments = readlines(file)
close(file)

function parse_experiment(str)
    return [parse(Int64, x) for x in split(str, ",")]
end

# Calculate the minimum matrix multiplication representation
# for each experiment
for experiment in experiments
    D = parse_experiment(experiment)
    println(min_mat_mul(D))
end
