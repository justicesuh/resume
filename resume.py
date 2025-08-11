import yaml


def main():
    with open('resume.yaml', 'r') as f:
        data = yaml.safe_load(f)
    print(data)


if __name__ == '__main__':
    main()
