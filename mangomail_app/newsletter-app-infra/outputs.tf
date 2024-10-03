output "vpc_id" {
  value       = aws_vpc.vpc1
  description = "The ID of the VPC"
}

output "eks_cluster_endpoint" {
  value       = aws_eks_cluster.n-cluster
  description = "The EKS cluster endpoint URL."
}

output "eks_cluster_security_group_ids" {
  value       = aws_eks_cluster.n-cluster
  description = "The security group IDs associated with the EKS cluster."
}

output "ecr_repository_url" {
  value       = aws_ecr_repository.my_ecr_repository.repository_url
  description = "The URL of the ECR repository."
}