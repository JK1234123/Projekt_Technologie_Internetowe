const { expect } = require('chai');
const { addPost } = require('./script');
const { addZdjecie } = require('./script');
const { filterPosts } = require('./script');
const { makeZdjecia } = require('./script');
const { makePosts } = require('./script');

describe('Forum', () => {
    it('should add a new post to the list', () => {
        const updatedPostList = addPost('Test title', 'Test content');
        expect(updatedPostList).to.equal(1)
    });
});
describe('Forum', () => {
    it('should add a new image to the list', () => {
        const updatedPostList = addZdjecie('Test title', 'Test url');
        expect(updatedPostList).to.equal(1)
    });
});
describe('Forum', () => {
    it('should add a new image to the list', () => {
        const updatedPostList = filterPosts();
        expect(updatedPostList).to.equal(1)
    });
});
describe('Forum', () => {
    it('should add a new image to the list', () => {
        const updatedPostList = makeZdjecia();
        expect(updatedPostList).to.equal(1)
    });
});
describe('Forum', () => {
    it('should add a new image to the list', () => {
        const updatedPostList = makePosts();
        expect(updatedPostList).to.equal(1)
    });
});