#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Our SIS application continues to be a success.  Educators actively use
the system to manage their students.  However, user feedback indicates
being able to organize students by natural filters such as school or
grade level isn't sufficient.  We must support a new "groups" feature.

Users must be able to...
- create new groups.
- specify a name when creating a new group.
- uniquely identify a group.*
- view a group's students.
- add a student to an existing group.

Users must NOT be able to...
- create a new group without specifying a name.
- create a new group with the same name as an existing group.
- add a student to the same group more than once.

Developers must be able to...
- view every object's documentation.
- view every object's representation.


* Check with me regarding your implementation because the unit tests
  are hard-coded.
"""


class Students(object):

    def __init__(self, first_name, last_name):

        """
        Students model.

        Parameters
        ----------
        first_name : str
            Forename.
        last_name : str
            Surname.

        Attributes
        ----------
        first_name : str
            Forename.
        last_name : str
            Surname.
        """

        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        repr_ = '{class_}(first_name="{first_name}", last_name="{last_name}")'
        return repr_.format(class_=self.__class__.__name__,
                            first_name=self.first_name,
                            last_name=self.last_name)


class TestStudentGroups(object):

    def test_create_group(self):
        StudentGroups(name='foo')

    @raises(TypeError)
    def test_create_group_missing_argument(self):
        StudentGroups()

    @raises(ValueError)
    def test_create_multiple_groups_with_same_name(self):
        StudentGroups(name='foo')
        StudentGroups(name='foo')

    def test_id(self):
        student_group = StudentGroups(name='foo')
        assert_equal(type(student_group.id), int)

    def test_id_is_unique(self):
        student_group_ids = [StudentGroups(name=str(i)).id for i in range(5)]
        assert_equal(len(student_group_ids), len(set(student_group_ids)))

    def test_id_is_not_null(self):
        student_group_ids = [StudentGroups(name=str(i)).id for i in range(5)]
        assert_true(all(student_group_id is not None
                        for student_group_id
                        in student_group_ids))

    def test_view_all_students(self):
        student_1 = Students(first_name='foo', last_name='bar')
        student_2 = Students(first_name='eggs', last_name='ham')
        student_group = StudentGroups(name='foobar')

        student_group.add(student=student_1)
        student_group.add(student=student_2)

        assert_equal(type(student_group.get_all()), list)
        assert_true(all(type(student) is Students
                        for student
                        in student_group.get_all()))

    def test_add_student(self):
        student = Students(first_name='foo', last_name='bar')
        student_group = StudentGroups(name='foobar')

        assert_false(student_group.get_all())

        student_group.add(student=student)

        assert_equal(student_group.get_all()[0], student)

    @raises(ValueError)
    def test_add_student_more_than_once(self):
        student = Students(first_name='foo', last_name='bar')
        student_group = StudentGroups(name='foobar')

        student_group.add(student=student)
        student_group.add(student=student)

    def teardown(self):
        StudentGroups._index = list()
        StudentGroups._sequence_next_value = 0

