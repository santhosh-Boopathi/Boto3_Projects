from operation import create_bucket_if_not_exists, upload_index_html

def main():
    create_bucket_if_not_exists()
    upload_index_html()
    # print(f'Static website hosted at http://{BUCKET_NAME}.s3-website-{REGION_NAME}.amazonaws.com')

if __name__ == '__main__':
    main()
