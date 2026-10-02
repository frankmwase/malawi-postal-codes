const test = require('node:test');
const assert = require('node:assert/strict');
const source = require('../../data/codes.json');
const { codes, findByCity, findByCode } = require('../dist/index.js');

test('generated records match the JSON source', () => {
  assert.deepEqual(codes, source);
});

test('every code resolves in both directions', () => {
  for (const entry of source) {
    assert.deepEqual(findByCity(entry.city.toUpperCase()), entry);
    assert.deepEqual(findByCode(entry.code), entry);
  }
});

test('unknown values return undefined', () => {
  assert.equal(findByCity('unknown town'), undefined);
  assert.equal(findByCode('9999'), undefined);
});
