## How to run

If necessary, activate your poetry virtual enviroment.

The workspace consists of two scripts: open-interest and scan-extensions. 

### Open Interest Script
This function obtains the open interest for each contract from the CFTC website and prints it to the console in the format "name_of_contract,open_interest".
To run the script, run:

`poetry run open-interest` from the working directory

For example:

`$ poetry run open-interest
CBL NATURE GLOBAL EMISSIONS,10411
CBL GLOBAL EMISSIONS OFFSET,12817
NY HARBOR ULSD,330825
UP DOWN GC ULSD VS HO SPR,31190
NAT GAS NYME,33936
...
`

For CLI help, you can run:

`poetry run open-interest --help`

### Scan Extensions Script
This script scans a directory and returns the number of files, the largest file, and the total size of all files for each file extension.
To run this script, run:

`poetry run  poetry run scan-extensions <PATH>`

where <PATH> is the directory you wish to scan, eg: /home/developer/side-projects/xantiu

For example:

`$poetry run scan-extensions /home/developer/side-projects/xantiu
                0         1         2
.md             3      4626      9660
.toml           2     23341     23825
.lock           1     31682     31682
             1286   8224336  18164134
.cfg            2       233       281
.py          2637    451104  37655008`

## Disclosure
I ran out of time to add tests or do any manual testing.
I might have considered adding some debug logs in addition.

### Things I thought of but didn't have time to think about deeply
- files without file extension are being recorded, is that appropriate?

## How to test
To be completed.

## Development

This project uses poetry for dependency management.

### Use `poetry` to specify project dependencies

Install poetry:
    
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

Install project requirements:

    poetry install

Add dependency:

    poetry add package

## Design Choices
The file we're running upon consists of sections, each section corresponding to a futures contract. The below is a sample snippet of two futures contracts:


=================================================================================
CBL NATURE GLOBAL EMISSIONS - NEW YORK MERCANTILE EXCHANGE           Code-00665T
FUTURES ONLY POSITIONS AS OF 10/03/23                         |
--------------------------------------------------------------| NONREPORTABLE
      NON-COMMERCIAL      |   COMMERCIAL    |      TOTAL      |   POSITIONS
--------------------------|-----------------|-----------------|-----------------
  LONG  | SHORT  |SPREADS |  LONG  | SHORT  |  LONG  | SHORT  |  LONG  | SHORT
--------------------------------------------------------------------------------
(CONTRACTS OF 1,000 ENVIRONMENTAL OFFSET             OPEN INTEREST:       10,411
COMMITMENTS
   5,449    3,446      550    4,282    6,376   10,281   10,372      130       39

CHANGES FROM 09/26/23 (CHANGE IN OPEN INTEREST:        -60)
    -103      399       50       14     -502      -39      -53      -21       -7

PERCENT OF OPEN INTEREST FOR EACH CATEGORY OF TRADERS
    52.3     33.1      5.3     41.1     61.2     98.8     99.6      1.2      0.4

NUMBER OF TRADERS IN EACH CATEGORY (TOTAL TRADERS:       51)
      18        9        7       19       15       40       28                  
 
 
CBL GLOBAL EMISSIONS OFFSET - NEW YORK MERCANTILE EXCHANGE           Code-006NJZ
FUTURES ONLY POSITIONS AS OF 10/03/23                         |
--------------------------------------------------------------| NONREPORTABLE
      NON-COMMERCIAL      |   COMMERCIAL    |      TOTAL      |   POSITIONS
--------------------------|-----------------|-----------------|-----------------
  LONG  | SHORT  |SPREADS |  LONG  | SHORT  |  LONG  | SHORT  |  LONG  | SHORT
--------------------------------------------------------------------------------
(CONTRACTS OF 1,000 ENVIRONMENTAL OFFSET             OPEN INTEREST:       12,817
COMMITMENTS
   2,644      885    4,631    5,372    7,239   12,647   12,755      170       62

CHANGES FROM 09/26/23 (CHANGE IN OPEN INTEREST:       -116)
    -190     -107       72       -4      -85     -122     -120        6        4

PERCENT OF OPEN INTEREST FOR EACH CATEGORY OF TRADERS
    20.6      6.9     36.1     41.9     56.5     98.7     99.5      1.3      0.5

NUMBER OF TRADERS IN EACH CATEGORY (TOTAL TRADERS:       42)
      16        9        6       12       13       30       26                  
==================================================================================

Three questions which impact the code design are:
    1) Is the number of lines for each contract section the same?
    2) Will that number ever change?
    3) Will the positioning of OPEN INTEREST within the snippet ever move?

I expect it would be safe to assume all three of these things- getting confirmation from the file owners would be the next step. That being said, it's simple enough to not make these assumptions, and should mean the code is more robust to future changes to the structure of the file its run on.
