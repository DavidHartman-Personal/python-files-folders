import os
# note that only last suffix returned
filename, file_extension = os.path.splitext('/path/to/somefile.ext')
# filename = '/path/to/somefile'
# file_extension = '.ext'

filename2, file_extension2 = os.path.splitext('/path/to/somefile.tar.gz')
# filename2 = '/path/to/somefile'
# file_extension2 = '.gz'