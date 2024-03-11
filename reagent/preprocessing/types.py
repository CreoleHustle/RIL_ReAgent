#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

# pyre-unsafe


class InputColumn:
    STATE_FEATURES = "state_features"
    STATE_SEQUENCE_FEATURES = "state_sequence_features"
    STATE_ID_LIST_FEATURES = "state_id_list_features"
    STATE_ID_SCORE_LIST_FEATURES = "state_id_score_list_features"
    NEXT_STATE_FEATURES = "next_state_features"
    NEXT_STATE_SEQUENCE_FEATURES = "next_state_sequence_features"
    NEXT_STATE_ID_LIST_FEATURES = "next_state_id_list_features"
    NEXT_STATE_ID_SCORE_LIST_FEATURES = "next_state_id_score_list_features"
    ACTION = "action"
    NEXT_ACTION = "next_action"
    ACTION_ID_LIST_FEATURES = "action_id_list_features"
    ACTION_ID_SCORE_LIST_FEATURES = "action_id_score_list_features"
    NEXT_ACTION_ID_LIST_FEATURES = "next_action_id_list_features"
    NEXT_ACTION_ID_SCORE_LIST_FEATURES = "next_action_id_score_list_features"
    POSSIBLE_ACTIONS = "possible_actions"
    POSSIBLE_ACTIONS_MASK = "possible_actions_mask"
    POSSIBLE_NEXT_ACTIONS = "possible_next_actions"
    POSSIBLE_NEXT_ACTIONS_MASK = "possible_next_actions_mask"
    NOT_TERMINAL = "not_terminal"
    STEP = "step"
    TIME_DIFF = "time_diff"
    TIME_SINCE_FIRST = "time_since_first"
    MDP_ID = "mdp_id"
    SEQUENCE_NUMBER = "sequence_number"
    METRICS = "metrics"
    REWARD = "reward"
    ACTION_PROBABILITY = "action_probability"
    SLATE_REWARD = "slate_reward"
    POSITION_REWARD = "position_reward"
    CANDIDATE_FEATURES = "candidate_features"
    NEXT_CANDIDATE_FEATURES = "next_candidate_features"
    REWARD_MASK = "reward_mask"
    ITEM_MASK = "item_mask"
    NEXT_ITEM_MASK = "next_item_mask"
    ITEM_PROBABILITY = "item_probability"
    NEXT_ITEM_PROBABILITY = "next_item_probability"
    EXTRAS = "extras"
    SCORES = "scores"
    VALID_STEP = "valid_step"
    WEIGHT = "weight"
    CONTEXT_FEATURES = "context_features"
    ARM_FEATURES = "arm_features"
    CONTEXT_ARM_FEATURES = "context_arm_features"
    ARMS = "arms"
    ARM_PRESENCE = "arm_presence"
    ACTION_LOG_PROBABILITY = "action_log_probability"
    LABEL = "label"
