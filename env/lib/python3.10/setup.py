from setuptools import setup, find_packages

setup(
    name='stock_trade_tracker',
    version='0.1.0',
    description='A stock trade tracker application with a CLI and web interface.',
    author='Your Name',
    author_email='your.email@example.com',
    url='http://example.com',
    packages=find_packages(),  # Automatically find all packages in the current directory
    install_requires=[
        'Flask>=2.0.0',
        'Flask-SQLAlchemy>=3.0.0',
        'Flask-Cors>=3.0.0',
        'pandas>=2.0.0',  # Optional, if you're using pandas
        'python-dotenv>=0.21.0'  # Optional, for environment variable management
    ],
    entry_points={
        'console_scripts': [
            'run-app=app:main',  # Replace 'app:main' with the correct module and function to run your app
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',
)
