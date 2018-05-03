import itertools, warnings, os, shlex, re
import HTSeq
from HTSeq import _HTSeq
_re_attr_main = re.compile( "\s*([^\s\=]+)[\s=]+(.*)" )
_re_attr_empty = re.compile( "^\s*$" )
def parse_GFF_attribute_string( attrStr, extra_return_first_value=False ):
   """Parses a GFF attribute string and returns it as a dictionary.
   
   If 'extra_return_first_value' is set, a pair is returned: the dictionary
   and the value of the first attribute. This might be useful if this is the ID.
   """
   if attrStr.endswith( "\n" ):
      attrStr = attrStr[:-1]
   d = {}
   first_val = "_unnamed_"
   for (i, attr) in itertools.izip( itertools.count(), _HTSeq.quotesafe_split( attrStr ) ):
      if _re_attr_empty.match( attr ):
         continue
      if attr.count( '"' ) not in ( 0, 2 ):
         raise ValueError, "The attribute string seems to contain mismatched quotes."
      mo = _re_attr_main.match( attr )
      if not mo:
         raise ValueError, "Failure parsing GFF attribute line"
      val = mo.group(2)
      if val.startswith( '"' ) and val.endswith( '"' ):
         val = val[1:-1]
      #val = urllib.unquote( val )
      d[ intern(mo.group(1)) ] = intern(val)
      if extra_return_first_value and i == 0:
         first_val = val         
   if extra_return_first_value:
      return ( d, first_val )
   else:
      return d

print parse_GFF_attribute_string('gene_id "WASH7P"; gene_name "WASH7P"; transcript_id "NR_024540"; tss_id "TSS8568";', True)
print parse_GFF_attribute_string('transcript_id "A172.4.9"; gene_id "A172.4";',True)
