module "vpc" {
  source = "../../modules/vpc"
}

module "sg" {
  source = "../../modules/sg"

  vpc_subnet_cigar_crawler_private_a_cidr_block = module.vpc.subnet_cigar_crawler_private_a_cidr_block
  vpc_subnet_cigar_crawler_private_c_cidr_block = module.vpc.subnet_cigar_crawler_private_c_cidr_block
  vpc_subnet_cigar_crawler_public_a_cidr_block  = module.vpc.subnet_cigar_crawler_public_a_cidr_block
  vpc_subnet_cigar_crawler_public_c_cidr_block  = module.vpc.subnet_cigar_crawler_public_c_cidr_block
  vpc_vpc_cigar_crawler_id                      = module.vpc.vpc_cigar_crawler_id
}

module "ecs" {
  source = "../../modules/ecs"
}

module "ecr" {
  source = "../../modules/ecr"
}
