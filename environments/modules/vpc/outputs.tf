output "vpc_cigar_crawler_id" {
  value = "${aws_vpc.cigar_crawler.id}"
}

output "subnet_cigar_crawler_public_a_id" {
  value = aws_subnet.cigar_crawler_public_a.id
}

output "subnet_cigar_crawler_public_c_id" {
  value = aws_subnet.cigar_crawler_public_c.id
}

output "subnet_cigar_crawler_public_a_cidr_block" {
  value = aws_subnet.cigar_crawler_public_a.cidr_block
}

output "subnet_cigar_crawler_public_c_cidr_block" {
  value = aws_subnet.cigar_crawler_public_c.cidr_block
}

output "subnet_cigar_crawler_private_a_cidr_block" {
  value = aws_subnet.cigar_crawler_private_a.cidr_block
}

output "subnet_cigar_crawler_private_c_cidr_block" {
  value = aws_subnet.cigar_crawler_private_c.cidr_block
}
