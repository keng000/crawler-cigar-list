output "cigar_crawler_private_subnet_all_tcp_id" {
  value = aws_security_group.cigar_crawler_private_subnet_all_tcp.id
}

output "cigar_crawler_public_subnet_all_tcp_id" {
  value = aws_security_group.cigar_crawler_public_subnet_all_tcp.id
}

output "cigar_crawler_ecs_id" {
  value = aws_security_group.cigar_crawler_ecs.id
}
