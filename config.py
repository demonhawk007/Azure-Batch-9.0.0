# -------------------------------------------------------------------------
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
# ----------------------------------------------------------------------------------
# The example companies, organizations, products, domain names,
# e-mail addresses, logos, people, places, and events depicted
# herein are fictitious. No association with any real company,
# organization, product, domain name, email address, logo, person,
# places, or events is intended or should be inferred.
# --------------------------------------------------------------------------

# Global constant variables (Azure Storage account/Batch details)

# import "config.py" in "python_quickstart_client.py "
subscription_id = 'd3372d19-3446-4221-9a34-b341b0ab0431'
_BATCH_ACCOUNT_NAME = 'azuremgmtbat'  # Your batch account name
_BATCH_ACCOUNT_KEY = 'LA/jGTiSAjhzDfi66qiwqGgwZnpTK1rGRB8yD+BCYKCu8cH/Eg8m7hTiaR7SBujJ4DrCDqIlJ/7gJtvFxqZDnA=='  # Your batch account key
_BATCH_ACCOUNT_URL = 'https://azuremgmtbat.eastus.batch.azure.com'  # Your batch account URL
_STORAGE_ACCOUNT_NAME = 'azuremgmt07172020'  # Your storage account name
_STORAGE_ACCOUNT_KEY = 'vQHYE2lyuwjf1SW3ZO71Qlsf3r/aVSV1UZE0lrzSjJeS0Dk6UgPw2j80PhidA2Ovb6OHZL5qoh+LKhIAw3HRNQ=='  # Your storage account key
storage_connection_string = 'DefaultEndpointsProtocol=https;AccountName=azuremgmt07172020;AccountKey=vQHYE2lyuwjf1SW3ZO71Qlsf3r/aVSV1UZE0lrzSjJeS0Dk6UgPw2j80PhidA2Ovb6OHZL5qoh+LKhIAw3HRNQ==;EndpointSuffix=core.windows.net'
_POOL_ID = 'PythonQuickstartPool'  # Your Pool ID
_POOL_NODE_COUNT = 2  # Pool node count
_POOL_VM_SIZE = 'STANDARD_A1_v2'  # VM Type/Size
_JOB_ID = 'PythonQuickstartJob'  # Job ID
_STANDARD_OUT_FILE_NAME = 'stdout.txt'  # Standard Output file
