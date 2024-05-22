import setuptools


# 종속 패키지 파싱
def package_text_parser(line: str):
    line = line.strip()
    if line.startswith("#") or line == "":
        return ""
    else:
        return line.split("#")[0]


required_packages = []

with open("requirements.txt", "rt", encoding="utf-8") as f:
    lines = f.read().splitlines()

for line in lines:
    line = package_text_parser(line)
    if line != "":
        required_packages.append(line)

# Setup
setuptools.setup(
    name="rpc",
    version="0.1.0",
    author="YeJun, Jung",
    description="Json RPC with Kafka",
    install_requires=required_packages,
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "rpc=rpc.cli:main"
        ]
    },
)
