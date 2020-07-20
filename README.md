# Misc scripts

Details to access the wiki are in `wikitails.yml`
* empty user and passwords: only give read access
* if you add user and password MAKE SURE NOT TO COMMIT IT :p
   
### Use [confIDent/mediawikitools](https://github.com/TIBHannover/confiDent-mediawikitools/)
Clone:
* `git clone https://github.com/TIBHannover/confiDent-mediawikitools.git`
* `cd confiDent-mediawikitools`

Install:
* using a venv `python setup.py install` 
* without venv, but as regular user: `python setup.py install --user` 
* system wide: `sudo python setup.py install`



### Test ask
`python test_ask.py`