#Question: Find all email addresses in a paragraph
import re
para="""For any questions, you can contact us at support@example.com, sales@example.org, info@company.net, or admin@website.com. 
You can also reach our customer service team at helpdesk@service.in and our manager at manager@business.co.uk.
 We will respond to your email as soon as possible.
"""
pattern=re.compile(r"[a-zA-z0-9]+@+[a-z.]+[a-z]")
result=re.findall(pattern,para)
pat=re.compile(r"[\w._*]+@+[\w.*]+[\w*]")
rst=re.findall(pat,para)
print(f"Emails are :{result}")
print(f"Emails given are :{rst}")
