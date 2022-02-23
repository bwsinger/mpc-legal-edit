# mpc-legal-edit
A command line tool used to remove legal text from proxy Magic the Gathering cards.

## Currently specific to just the legal text appended to Card Conjurer images
https://cardconjurer.com/creator/

<b>Before and After</b>
<div style="display: flex;">
  <img src="https://user-images.githubusercontent.com/16724046/155317057-bc5b49d3-9c21-48d1-b3d6-b7b9acada9fd.png" width="300">
  <img src="https://user-images.githubusercontent.com/16724046/155317115-2e867be2-7d87-48a1-855b-be8990b85a01.png" width="300">
</div>

## Operation
Requires Python3

Example:
```
~ python3 remove_legal.py path/to/proxy/images/
```
Creates a new directory `path/to/proxy/images/removed_legal` (can be changed with `-o` parameter) with the edited images.
