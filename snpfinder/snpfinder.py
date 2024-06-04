#!/usr/bin/env python3

"""
Command-line script to perform variant calling of pileup files

Similar to VarScan mpileup2snp
"""

import argparse
from . import myutils as myutils


def main():
    parser = argparse.ArgumentParser(
        prog="snpfinder",
        description="Command-line script to perform variant calling of mpileup files"
    )

    # Input
    parser.add_argument("mpileup", help="mpileup file", type=str)

    # Output
    parser.add_argument("-o", "--out", help="Write output to file. " \
                        "Default: stdout", metavar="FILE", type=str, required=False)

    # Optional arguments
    parser.add_argument("--min_var_freq", help="minimum proportion of non-reference bases at a position required to call it a variant", type=float, required=False, default=0.2)

    parser.add_argument("--min_hom_freq", help="minimum proportion of non-reference bases at a position required to call a variant homozygous", type=float, required=False, default=0.8)
    
    args = parser.parse_args()

    variants = myutils.call_variants(args.mpileup, args.min_var_freq, args.min_hom_freq)

    # set default output file name if --out is not provided
    output_file = args.out if args.out else "output.vcf"

    myutils.build_vcf(variants, output_file)

if __name__ == "__main__":
    main()
