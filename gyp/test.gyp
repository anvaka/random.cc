{
  'includes': [
    './common.gypi'
  ],
  'targets': [
    {
      'target_name': 'test',
      'type': 'executable',
      'dependencies': [
        './random.cc.gyp:*',
        "<!(node -e \"console.log(require.resolve('catch.cc/gyp/catch.cc.gyp') + ':*')\")",
      ],
      'sources': [
        '../test/main.cc'
      ],
    }
  ]
}
