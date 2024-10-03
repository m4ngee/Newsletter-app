provider "aws" {
    region = var.aws_region
  
}

resource "aws_vpc" "vpc1" {

    cidr_block = var.vpc_cidr_block
    enable_dns_hostnames = true
    enable_dns_support = true

    tags = {
      Name = "vpc1"
    }
  
}

resource "aws_subnet" "public_subnets" {
    count = length(var.public_subnet_cidr_blocks)

    vpc_id = aws_vpc.vpc1.id
    cidr_block = var.public_subnet_cidr_blocks[count.index]

    availability_zone = element(data.aws_availability_zones.available.names, count.index)

    tags = {
      Name = "PublicSubnet${count.index +1}"
    }

}

data "aws_availability_zones" "available" {
    state = "available"
  
}

resource "aws_eks_cluster" "n-cluster" {
    name = var.eks_cluster_name
    role_arn = aws_iam_role.eks_cluster.arn

    vpc_config {
      subnet_ids = aws_subnet.public_subnets[*].id
    }
  
}
resource "aws_iam_role" "eks_cluster" {
    name = "eks-cluster-role"

    assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "eks.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_user" "admin-user" {
    name = "mango1"
  
}

resource "aws_iam_user_policy_attachment" "eks_cluster_policy" {
    user = aws_iam_user.admin-user.name
    policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"


  
}

# Create an Elastic Container Registry (ECR)
resource "aws_ecr_repository" "my_ecr_repository" {
  name = var.ecr_repository_name

  image_tag_mutability = "IMMUTABLE"
}

