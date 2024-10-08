variable "aws_region" {
  description = "The AWS region where the resources will be created."
  default     = "eu-west-2"
}

variable "vpc_cidr_block" {
  description = "The CIDR block for the VPC"
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr_blocks" {
  description = "The CIDR blocks for the public subnets."
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}

variable "eks_cluster_name" {
  description = "The name of the EKS cluster."
  default     = "Newsletter-cluster"
}

variable "ecr_repository_name" {
  description = "The name of the ECR repository."
  default     = "my-ecr-repository"
}


