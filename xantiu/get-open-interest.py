import requests
import click

OPEN_INTEREST_DELIMITER = "OPEN INTEREST: "
LINE_OF_OPEN_INTEREST_DELIMITER = "CONTRACTS OF"
START_OF_CONTRACT_DELIMITER = "FUTURES ONLY"
NAME_OF_CONTRACT_DELIMITER = " - NEW YORK MERCANTILE EXCHANGE"

@click.command()
def get_open_interest():
    '''
    This function obtains the open interest for each contract from the CFTC website and prints it to the console in the format "name_of_contract,open_interest".
    '''
    url = "https://www.cftc.gov/dea/futures/deanymesf.htm"
    #Download the content from the URL
    r = requests.get(url)
    #Split the content into lines
    lines = r.text.splitlines()
    #Traverse the lines, searching first for the string that indicates the start of a new contract section <START_OF_CONTRACT_DELIMITER>, and then the string that indicates the start of the open interest line <LINE_OF_OPEN_INTEREST_DELIMITER>.
    while True:
        #We put the try/except here because we want to break out of the loop when we reach the end of the file.
        try:
            #Obtain the line number of the line that contains the name of the contract.
            first_line_idx = index_searcher_for_substr(lines, START_OF_CONTRACT_DELIMITER) - 1
        #We hit this TypeError if index_searcher_for_substr returns an EOFError, at which point we break the loop as we've reached the end of the file.
        except TypeError:
            break
        #Obtain the name of the contract by splitting the line on the delimiter and taking the first element of the resulting list.
        name_of_contract = lines[first_line_idx].split(NAME_OF_CONTRACT_DELIMITER)[0]
        #Obtain the line number of the line that contains the open interest
        first_open_idx = index_searcher_for_substr(lines, LINE_OF_OPEN_INTEREST_DELIMITER)
        #.strip() removes the blank space whilst .replace(",", "") removes the commas from the number.
        open_contract = lines[first_open_idx].split(OPEN_INTEREST_DELIMITER)[1].strip().replace(",", "")
        print(name_of_contract + "," + open_contract)
        #Update lines to only contain the lines below the contract we've just analyzed.
        lines = lines[first_open_idx+1:]


def index_searcher_for_substr(lines, str):
        '''
        This function searches for a substring in a list of strings and returns the index of the first occurrence of that substring.
        Returns an EOFError if the substring is not found.
        '''
        for (idx, line) in enumerate(lines):
            if str in line:
                return idx
        return EOFError("No more lines to search for " + str)
