
# Description 

Scrapy for cuban cigar website.

This is a application to get an updates of [Cuban Cigar Website](https://www.cubancigarwebsite.com/).

All updates will post to [This Blog](https://cigar-kengo000.hatenablog.com/).

 
## Environments

This is a batch application and it's hosted on [AWS Fargate](https://aws.amazon.com/fargate/).

AWS Environments are provisioned by [Terraform](https://www.terraform.io/).

All scrapings are implemented with [Scrapy](https://scrapy.org/) and all of the workflow are build with [Luigi](https://github.com/spotify/luigi).

# TODO

- [x] post an updates to a public blog
- [ ] post an updates to a mailing-list