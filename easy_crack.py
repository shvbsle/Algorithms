# some puzzle that I'm supposed to crack

s = """aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vZm9ybXMvZC9lLzFGQUlwUUxTZFYwWWtxdkFmTVFCRGxET3BWNW9hbFNxUWczUnJIYnhqbXRMa1Q1TFQ0QW5RZFBnL3ZpZXdmb3JtCg"""
import base64
# add padding
coded_string = s+"=="
print(base64.b64decode(coded_string))