#!/usr/bin/env python3
"""
KnowledgeTree 部署文件检查脚本
验证所有部署所需的文件是否完整
"""

import os
import sys
from pathlib import Path

def check_files():
    """检查部署所需的文件"""
    
    root_dir = Path(__file__).parent
    
    # 定义需要检查的文件
    required_files = {
        # 部署脚本
        "脚本文件": {
            "deploy.sh": "Linux/Mac自动化部署脚本",
            "deploy.ps1": "Windows自动化部署脚本",
        },
        
        # 文档
        "快速指南": {
            "QUICK_DEPLOYMENT.md": "5分钟快速开始（强烈推荐）",
            "DEPLOYMENT_RESOURCES.md": "部署资源完整清单（你现在看的）",
            "DEPLOYMENT_CHECKLIST.md": "部署前后检查清单",
        },
        
        # 详细文档
        "详细文档": {
            "DEPLOYMENT_GUIDE.md": "完整部署指南（600+行）",
            "QUICK_REFERENCE.md": "API速查表 + 常见问题",
            "DOCUMENT_PROCESSING_GUIDE.md": "功能处理指南",
        },
        
        # 配置文件
        "配置文件": {
            ".env.example": "环境变量模板",
            "nginx.conf": "Nginx反向代理配置",
            "requirements.txt": "Python依赖列表",
        },
        
        # 核心代码
        "核心代码": {
            "knowledge-compiler/server.py": "FastAPI主服务",
            "knowledge-compiler/parser/text_extractor.py": "文本提取模块",
            "knowledge-compiler/parser/llm_structurer.py": "LLM结构化模块",
        },
    }
    
    print("\n" + "="*60)
    print("🔍 KnowledgeTree 部署文件检查")
    print("="*60 + "\n")
    
    total_files = 0
    found_files = 0
    
    # 检查每个分类
    for category, files in required_files.items():
        print(f"\n📂 {category}")
        print("-" * 60)
        
        for filename, description in files.items():
            filepath = root_dir / filename
            total_files += 1
            
            if filepath.exists():
                found_files += 1
                status = "✅"
                size = filepath.stat().st_size
                size_str = f"{size/1024:.1f}KB" if size < 1024*1024 else f"{size/(1024*1024):.1f}MB"
                print(f"{status} {filename:<40} ({size_str})")
                print(f"   └─ {description}")
            else:
                status = "❌"
                print(f"{status} {filename:<40} [未找到]")
                print(f"   └─ {description}")
        
        print()
    
    # 总结
    print("="*60)
    print(f"\n📊 检查结果: {found_files}/{total_files} 文件就位")
    
    if found_files == total_files:
        print("\n✅ 所有部署文件都已就位！")
        print("\n🚀 下一步:")
        print("   1. 打开 QUICK_DEPLOYMENT.md 选择部署方案")
        print("   2. 准备 DeepSeek API 密钥")
        print("   3. 运行部署脚本")
        print("\n💡 快速命令:")
        print("   # Linux/Mac:")
        print("   bash deploy.sh docker 'your_api_key'")
        print("\n   # Windows (PowerShell):")
        print("   .\\deploy.ps1 -DeployType docker -ApiKey 'your_api_key'")
        return 0
    else:
        missing = total_files - found_files
        print(f"\n⚠️  缺少 {missing} 个文件")
        
        if missing > 0:
            print("\n❌ 缺失的文件需要从文档中创建或下载")
            print("\n📖 参考文档:")
            print("   - QUICK_DEPLOYMENT.md: 完整的部署指南")
            print("   - DEPLOYMENT_GUIDE.md: 详细的配置说明")
        
        return 1

def check_python_deps():
    """检查Python依赖"""
    print("\n\n" + "="*60)
    print("🐍 Python 依赖检查")
    print("="*60 + "\n")
    
    required_packages = [
        ("fastapi", "Web框架"),
        ("uvicorn", "ASGI服务器"),
        ("python-docx", "Word文档处理"),
        ("chardet", "编码检测"),
        ("httpx", "HTTP客户端"),
        ("pymupdf", "PDF处理"),
    ]
    
    found_packages = 0
    
    for package_name, description in required_packages:
        try:
            __import__(package_name.replace("-", "_"))
            found_packages += 1
            print(f"✅ {package_name:<20} {description}")
        except ImportError:
            print(f"❌ {package_name:<20} {description} [未安装]")
    
    print(f"\n📊 Python依赖: {found_packages}/{len(required_packages)} 已安装")
    
    if found_packages < len(required_packages):
        print("\n💡 安装依赖:")
        print("   pip install -r requirements.txt")

def main():
    """主函数"""
    
    # 检查文件
    file_result = check_files()
    
    # 检查Python依赖
    check_python_deps()
    
    # 部署建议
    print("\n\n" + "="*60)
    print("📋 部署建议")
    print("="*60 + "\n")
    
    print("1️⃣  快速部署 (推荐首选):")
    print("   • 最简单: Docker方案")
    print("   • 最稳定: Linux+Nginx方案")
    
    print("\n2️⃣  部署前准备:")
    print("   ✓ 获取 DeepSeek API 密钥")
    print("   ✓ 确保Docker已安装（或Python 3.8+）")
    print("   ✓ 阅读 QUICK_DEPLOYMENT.md")
    
    print("\n3️⃣  执行部署:")
    print("   # Docker (推荐):")
    print("   bash deploy.sh docker 'sk-your_api_key'")
    print("\n   # Linux传统部署:")
    print("   bash deploy.sh linux 'sk-your_api_key'")
    
    print("\n4️⃣  验证部署:")
    print("   curl http://localhost:8000/api/health")
    
    print("\n" + "="*60)
    print("📚 详细文档:")
    print("="*60)
    print("• QUICK_DEPLOYMENT.md     - 5分钟快速开始指南")
    print("• DEPLOYMENT_GUIDE.md     - 完整详细部署指南")
    print("• DEPLOYMENT_CHECKLIST.md - 部署前后检查清单")
    print("• QUICK_REFERENCE.md      - API速查表 + FAQ")
    print("\n")
    
    return file_result

if __name__ == "__main__":
    sys.exit(main())
