{
  'includes': [
    './common.gypi'
  ],
  'targets': [
    {
      'target_name': 'test',
      'type': 'executable',
      'dependencies': [
        './package.gyp:*',
        "<!(node -e \"console.log(require.resolve('catch.cc/gyp/package.gyp') + ':*')\")",
      ],
      'sources': [
        '../test/main.cc'
      ],
    }
  ]
}
