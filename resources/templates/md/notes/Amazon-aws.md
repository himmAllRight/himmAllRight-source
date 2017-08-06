Created my AWS Free account. Going to start learning some of this stuff over the
next year :)

Signed up. I'll start by going through Videos I guess...

Started working through the process of setting everything up to create an EC2 instance....

### Pre Run Setups
- I created a User + group
- I'm setting up Keys
  - Downloaded pair, changed permissions to 400
- Create VPC -- No sure if I need this yet, so I am going to skip it for now...

### EC2 Instance
- I created and launched a free instance through the wizard.
- When connecting, I was using ssh with the key `ssh -i keyname.pem ip` but getting a public key
  error. Then I realized I needed to specifiy the user name. In this case, `ssh -o key.pem
  ubuntu@ip`.

## 
