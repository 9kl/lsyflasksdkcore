# PyPI 发布指南

## 1. 环境准备

### 安装构建依赖
```bash
pip install build twine wheel
```

### 配置 PyPI 凭据
在用户目录创建 `~/.pypirc` 文件：

```ini
[distutils]
index-servers = pypi

[pypi]
username = __token__
password = <your-api-token>
```

或者使用环境变量：
```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=<your-api-token>
```

## 2. 构建包

```bash
# 清理之前的构建
rm -rf dist/ build/ *.egg-info/

# 构建包
python -m build
```

## 3. 检查包

```bash
# 检查包的完整性
python -m twine check dist/*
```

## 4. 测试上传（可选）

先上传到 TestPyPI 进行测试：

```bash
python -m twine upload --repository testpypi dist/*
```

测试安装：
```bash
pip install --index-url https://test.pypi.org/simple/ lsyflasksdkcore
```

## 5. 正式上传

```bash
python -m twine upload dist/*
```

## 6. 验证安装

```bash
pip install lsyflasksdkcore
```

## 版本管理

每次发布新版本时：

1. 更新 `setup.py` 中的版本号
2. 更新 `CHANGELOG.md`（如果有）
3. 提交代码并打标签
4. 重新构建和上传

```bash
# 更新版本后
git add .
git commit -m "Release version 1.0.1"
git tag v1.0.1
git push origin main --tags

# 重新构建
python -m build
python -m twine upload dist/*
```

## 注意事项

1. **API Token**: 在 PyPI 网站生成 API token，不要使用用户名密码
2. **版本号**: 每次上传必须使用新的版本号，不能覆盖已存在的版本
3. **描述**: 确保 README.md 使用正确的 Markdown 格式
4. **许可证**: 确保 LICENSE 文件包含在包中
5. **依赖**: 确保 requirements.txt 中的依赖版本兼容性

## 常见问题

### 构建失败
- 检查 setup.py 配置
- 确保所有必需文件存在
- 检查 MANIFEST.in 配置

### 上传失败
- 检查网络连接
- 验证 API token
- 确保版本号唯一
- 检查包名是否已被占用

### 安装失败
- 检查依赖冲突
- 验证 Python 版本兼容性
- 检查包的完整性