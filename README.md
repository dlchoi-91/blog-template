# blog-template

The repository contains a template for my blog to publish projects and other work related entries hosted at [imdanielchoi.com](https://imdanielchoi.com). The goal of this blog really is just for me to have fun with hosting a website and for me to publish projects that I work on so I can have them in a central location. This repository will be used to provide a template for how I manage my static site and directions if you wish to copy or use portions of it where you see fit. Note that all values in configs, content and other elements are left blank as this is only a template! Please review Pelican [documentation]("https://docs.getpelican.com/en/latest/#") for configuring your site to your liking!


## Set-up Dev Environment
In the event you need to setup your own computer for content writing and local development testing, make sure you have the following installed:
- conda == 4.9.2
- python == 3.9.2

These are just the versions of conda and python used to develop the website initially and haven't been tested with other versions. I used Git Bash as the terminal on Windows 10 Professional to execute commands locally. For versions of packages used, see the [requirements.txt](requirements.txt) file.

Assuming you created your own conda venv before, you can run the following commands to setup the virtual environment for development:

```bash
conda.bat activate pelican_dev #where pelican_dev is the environment you created. can omit if not using venv.
cd blog_template # or change to your personal repo directory
pip install -r requirements.txt
pelican-themes --symlink blog_template/pelican-themes/Flex
```


## Publishing Workflow
Content can be created using the Pelican [documentation]("https://docs.getpelican.com/en/latest/#"). A markdown file should be saved in the "content" directory. For reference pages that should not fall under project or content, a separate page can be published and saved under the "content/pages" directory. Once saved, you can run the following commands to run a local version of the file for initial testing:

```bash
pelican content -s pelicanconf.py
pelican --listen
```

You should then open up http://localhost:8000/ on your browser to ensure the pages you published are functioning correctly. Once validated, you can press `ctrl+c` in the console to exit. After validating locally, you should commit the repo and push to branch `content_write`.

Create a pull request from `content_write` to `main` and this will trigger the test github action. The [yml file can be found in the .github/workflow directory](.github/workflows/test.yml). This action builds the website using the test configuration file and publishes to the test bucket. Your test bucket link will be something like http://mytestbucket.com.s3-website-us-east-1.amazonaws.com/. Use the link to click through and make sure the content you published is showing and is to your liking.


There are two configuration files that are used based on environments you are using:
1. [pelicanconf.py](pelicanconf.py) - Used for local development and the test bucket for the test website. This configuration file has all the key configurations for the website and assumes relative references for testing purposes.
2. [publishconf.py](publishconf.py) - Used for production website. This configuration has all the key configuration in `pelicanconf.py`


Once the pull request is completed, the [production workflow action](.github/workflows/production.yml) will initiate and automatically create the output files and loads to the correct production bucket. The new pages might not be available immediately as CloudFront needs to obtain the objects from the bucket.

Note that the output directory is ignored in this repository as it is created in test and production through github actions.

The publishing workflow is completed after you complete the pull request! Make sure the actions completed succesfully and sit back and enjoy the new content.

## GitHub Variables Used
For the workflows to function, make sure you have the following variables configured in GitHub actions in the settings portion of the repo. The actions use these variables to assume the correct role and deploy to the correct buckets.
1. AWS_ASSUME_ROLE_ARN - ARN of the role you created that GitHub can assume to access your bucket.
2. AWS_REGION - The region in which you setup your buckets
3. PROD_BUCKET - The S3 link to your main S3 bucket (e.g. s3://mybucket.com)
4. TEST_BUCKET - The S3 link to your testing S3 bucket (e.g. s3://mytestbucket.ccom)

## AWS Resources
The following are the AWS resources that support the website. You can use GitHub pages for your site and is probably the best and easiest way to get your site running. I used S3 Static hosting simply because I wanted to play around with AWS.

##### AWS S3
1. Main S3 Bucket (e.g. s3://mybucket.com) - S3 bucket for website resource storage. The primary website is hosted in this bucket and CloudFront is connected to this bucket as the origin.
2. Reroute S3 Bucket (e.g. s3://www.mybucket.com)  - S3 bucket used to reroute traffic to imdanielchoi.com bucket. No objects should be stored in this bucket and should only be configured for reroutes.
3. Testing S3 Bucket (e.g. s3://mytestbucket.com) - S3 bucket used for testing. The test workflow loads files to this bucket to test on browser.

##### AWS Route 53
1. Hosted Zone - This is the hosted zone created by R53. The domain name is also registered through Route 53 and the service automatically creates the hosted zone. The domain name is set to renew every year.

##### AWS CloudFront
1. Distribution - Distribution for the website. Uses the imdanielchoi.com bucket as the origin and the certificate from Certificate Manager for the SSL Certificate.

##### AWS Certificate Manager
1. Certificate for the imdanielchoi.com domain that CloudFront uses for HTTPS connections.

#### AWS IAM
1. Role that GitHub actions can assume to deploy resources to your S3 buckets. Process to authorize GitHub using the assume role with web authentication call can be found in this [link](https://github.com/aws-actions/configure-aws-credentials#configure-aws-credentials-for-github-actions). You'll need to setup the OIDC provider and then setup the role and trust policy that points to the provider. The permissions you'll need to give the role are `s3:PutObject`,`s3:ListBucket`, and `s3:DeleteObject` to the two buckets you created.



