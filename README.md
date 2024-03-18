# Python_NanoBiTanalysis
For analysing and plotting NanoBiT data

NanoBiT assay is a type of luciferase complementation assay where NanoLuc is split into Small-BiT and Large-BiT. Here, SmBiT is fused to a COPII cargo adaptor protein SEC24A and LgBiT to a cargo receptor SURF4. By mutating various interaction sites on both proteins and assaying their effect on NanoLuc complementation signal, we can infer which sites are responsible for mediating the interaction between the two proteins. 

"surf4mut_all.csv" contains data of 3 biological replicates with 6 technical replicates each. "Nanobit.py" does the following:

1) reads the data and calculates averages of the 6 replicates
2) performs one-way t-test on the calculated averages, comparing control and SURF4 mutants to WT-SURF4
3) creates a plot displaying both the technical replicates and averages, as well as p-values
4) saves the plot
