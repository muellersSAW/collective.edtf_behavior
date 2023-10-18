Changelog
=========


2.0.0 (2023-10-18)
------------------

- using edtf2 package which implements the newest edtf specification (2019-02-04) [muellers]
- adjusting indexe to convert infinity results to datetime.min and datetime.max; in general the date_latest and date_earliest indexe are based on pythons datetime package where we have the 1 AD - 9999 AD limitation, so they are not useable for dates outside this limitation [muellers]

1.0.4 (2023-10-18)
------------------

- fixed wrong python_requires statement in setup.py [muellers]


1.0.3 (2019-08-26)
------------------

- Faxed test and test setup, small cleanup
  [MrTango]


1.0.2 (2019-03-22)
------------------

- Add edtf_parseable validator (constraint) to edtf_behavior
  [MrTango]


1.0.1 (2019-03-18)
------------------

- Add absolute_import statement to all files, to improve Py3 support, fix README syntax
  [MrTango]


1.0 (2019-03-18)
----------------

- Add edtf_start_end_range index and document querying in the readme.
  [MrTango]


1.0a1 (2019-03-14)
------------------

- Initial release, with EDTF behavior and 4 main indexes.
  [MrTango]
